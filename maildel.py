# -*- coding: utf-8 -*-
import getpass,poplib,sys

keepmail = 100
M = poplib.POP3('mailserver.example.com',port=110)
M.user('userid')
M.pass_('password')
numMessages = len(M.list()[1])
print('全メッセージ数:'+str(M.stat()[0]))
print('全メッセージサイズ:'+str(M.stat()[1]))

print('最新の'+str(keepmail)+'通を残してメールを削除してよろしいですか? (y/n)')
response = input()
if response != 'y':
    print('処理を中断して終了します')
    sys.exit()

if M.stat()[0] <= keepmail:
    print('メールサーバ上のメールが100通より少ないため終了します')
    M.quit()
    sys.exit()

print('最新'+str(keepmail)+'通を残してメールを削除します')
for i in range(numMessages-keepmail):
    print('メール'+str(i+1)+'を削除しています')
    M.dele(i+1)
          
M.quit()
