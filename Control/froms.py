#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django import forms


class RegisterForms(forms.Form):
    name = forms.CharField(error_messages={'required': u"用户名不能为空"}, max_length=64)
    email = forms.EmailField(error_messages={'required': u"请输入正确的邮箱格式"})
    passwd = forms.CharField(error_messages={'required': u"请输入密码"})
    repasswd = forms.CharField(error_messages={'required': u"请输入密码"})

    def clean(self):
        cleaned_data = super(Register, self).clean()
        passwd = cleaned_data.get('passwd')
        repasswd = cleaned_data.get('repasswd')
        if passwd != repasswd:
            msg = u"密码不一致"
            self._errors["repasswd"] = self.error_class([msg])
        return cleaned_data


class LoginForms(forms.Form):
    email = forms.EmailField(error_messages={'required': u"请输入正确的邮箱格式"})
    password = forms.CharField(error_messages={'required': u"请输入密码"})