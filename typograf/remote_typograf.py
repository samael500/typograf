# -*- encoding: utf-8 -*-

import xml
import xml.etree.cElementTree as ET
import xml.dom.minidom

import sys
import socket

PY3 = sys.version.startswith('3.')

if PY3:
    from io import BytesIO as Container
else:
    from StringIO import StringIO as Container


class RemoteTypograf(object):

    HOST = 'typograf.artlebedev.ru'
    SOAP_REQUEST = '''\
POST /webservices/typograf.asmx HTTP/1.1
Host: {host}
Content-Type: text/xml
Content-Length: {length}
SOAPAction: "http://typograf.artlebedev.ru/webservices/ProcessText"

{content}
'''

    def __init__(self, encoding='UTF-8', br=False, p=False, nobr=3, entityType=1, timeout=10):
        """
        :param encoding: - string
        :param br: - bool, use or not <br> tags
        :param p: - bool, use or not <p> tags
        :param nobr: - int, maximum word to nobr join
        :param entityType: - int, type of text content
        :param timeout: - int, timeout in second for socet connection
        """
        self._encoding = encoding
        self._entityType = entityType
        self._useBr = br
        self._useP = p
        self._maxNobr = nobr
        self._timeout = timeout

    def html_entities(self):
        """ set use html only """
        self._entityType = 1

    def xml_entities(self):
        """ set use xml only """
        self._entityType = 2

    def mixed_entities(self):
        """ set use all type """
        self._entityType = 4

    def no_entities(self):
        """ set use plain text """
        self._entityType = 3

    def br(self, value):
        """ set use <br /> """
        self._useBr = int(bool(value))

    def p(self, value):
        """ set use <p> *text* </p> """
        self._useP = int(bool(value))

    def nobr(self, value):
        """ set max word nobr """
        self._maxNobr = value or 0

    def __create_xml_request(self, text):
        """ make xml content from given text """
        # create base stucture
        soap_root = ET.Element('soap:Envelope', {
            'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xmlns:xsd': 'http://www.w3.org/2001/XMLSchema',
            'xmlns:soap': 'http://schemas.xmlsoap.org/soap/envelope/', })
        body = ET.SubElement(soap_root, 'soap:Body')
        process_text = ET.SubElement(body, 'ProcessText', {
            'xmlns': 'http://typograf.artlebedev.ru/webservices/', })
        # add contents
        ET.SubElement(process_text, 'text').text = text
        ET.SubElement(process_text, 'entityType').text = str(self._entityType)
        ET.SubElement(process_text, 'useBr').text = str(self._useBr)
        ET.SubElement(process_text, 'useP').text = str(self._useP)
        ET.SubElement(process_text, 'maxNobr').text = str(self._maxNobr)
        # create tree and write it
        string = Container()
        soap = ET.ElementTree(soap_root)
        soap.write(string, encoding=self._encoding, xml_declaration=True)
        if PY3:
            return string.getvalue().decode(self._encoding)
        return string.getvalue()

    def __parse_xml_response(self, response):
        """ parse response and get text result """
        # get xml from response
        xml_response = response[response.find('<?xml'):].replace(' encoding=""', '')
        xml_content = xml.dom.minidom.parseString(xml_response)
        return xml_content.getElementsByTagName('ProcessTextResult')[0].firstChild.nodeValue

    def process_text(self, text):
        """ send request with given text and get result """
        # escape base char
        text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        # make xml request body
        soap_body = self.__create_xml_request(text)
        # make total request
        length = len(soap_body.encode('UTF-8')) if PY3 else len(soap_body)
        soap_request = self.SOAP_REQUEST.format(
            length=length, host=self.HOST, content=soap_body)

        if PY3:  # convert to bytes
            soap_request = soap_request.encode(self._encoding)

        # send request use soket
        connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connector.settimeout(self._timeout)
        connector.connect((self.HOST, 80))
        connector.sendall(soap_request)
        # call for response
        response = b''
        buf = '0'
        while len(buf):
            buf = connector.recv(8192)
            response += buf
        connector.close()

        if PY3:  # convert to str
            response = response.decode()

        # parse response
        text_result = self.__parse_xml_response(response)
        # back replace and return
        return text_result.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')

    def try_process_text(self, text):
        """ safe process text if error - return not modifyed text """
        if not text:
            return text
        try:
            return self.process_text(text)
        except (socket.gaierror, socket.timeout, xml.parsers.expat.ExpatError):
            return text
