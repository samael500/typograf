# -*- encoding: utf-8 -*-

from unittest import TestCase
import socket


class TypografTestCase(TestCase):

    """ Test typograf class """

    test_text = '<<simple>> -- "Text" -- t test t'
    result_text = '<<simple>>&nbsp;&#151; &laquo;Text&raquo;&nbsp;&#151; t&nbsp;test&nbsp;t\n'

    @classmethod
    def setUpClass(cls):
        from typograf import RemoteTypograf
        cls.RemoteTypograf = RemoteTypograf

    def test_service_not_found(self):
        """ Check correct errors if not fount host """
        typograf = self.RemoteTypograf()
        # change host
        typograf.HOST = 'ab.cd.com'
        with self.assertRaises(socket.gaierror):
            typograf.process_text(self.test_text)
        # not error if safe method
        result = typograf.try_process_text(self.test_text)
        self.assertEquals(result, self.test_text)

    def test_timeout_errors(self):
        """ Check correct errors if timeout """
        typograf = self.RemoteTypograf(timeout=1)
        # change host
        typograf.HOST = '10.0.0.1'
        with self.assertRaises(socket.timeout):
            typograf.process_text(self.test_text)
        # not error if safe method
        result = typograf.try_process_text(self.test_text)
        self.assertEquals(result, self.test_text)

    def test_correct_response(self):
        """ check text was changed """
        typograf = self.RemoteTypograf()
        result = typograf.process_text(self.test_text)
        try_result = typograf.try_process_text(self.test_text)
        self.assertEquals(result, try_result)
        self.assertEquals(result, self.result_text)

    def test_paragraf_text(self):
        """ check text with paragraf """
        typograf = self.RemoteTypograf(p=True)
        result = typograf.process_text(self.test_text)
        self.assertIn('<p>', result)
        self.assertIn('</p>', result)
        # disable paragraf
        typograf.p(False)
        result = typograf.process_text(self.test_text)
        self.assertNotIn('<p>', result)
        self.assertNotIn('</p>', result)

    def test_linebreak_text(self):
        """ check text with linebreak """
        typograf = self.RemoteTypograf(br=True)
        result = typograf.process_text(self.test_text)
        self.assertIn('<br />', result)
        # disable paragraf
        typograf.br(False)
        result = typograf.process_text(self.test_text)
        self.assertNotIn('<br />', result)

    def test_no_double_escape(self):
        """ check text not re escaping """
        typograf = self.RemoteTypograf()
        result = typograf.process_text(self.result_text)
        self.assertEquals(result, self.result_text)
        # and again
        result = typograf.process_text(result)
        self.assertEquals(result, self.result_text)

    def test_example_str(self):
        text = u'"Вы все еще кое-как верстаете в "Ворде"? - Тогда мы идем к вам!"'
        res_text = u'''<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;\
Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>'''
        typograf = self.RemoteTypograf(p=True, br=True)
        typograf.html_entities()
        result = typograf.process_text(text)
        self.assertEquals(result, res_text)
