from time import sleep 

class wizard():
    def _init_(self):
        pass 

    def enter(interval):
        print('An odd approaching shape reveals itself to be...')
        sleep(interval)
        print("Nyahaheheh, it's me! Can you answer my riddles three?")
        sleep(interval)
    
    def exit(interval):
        print("Enough of this nonsense!")
        sleep(interval)
        print("*The wizard has left*")

    def happy():
        print(r"""
          *
        /   \
        ^ | ^
          V     *    
        #####  /
    """)
        
    def sad():
        print(r""" 
          *
        /   \
        v   v
          |
          ^
        ##### \
               *
        """)
    
EMOTE_INTERVAL = 1.25

odd_wizard = wizard 
wizard.enter(1.5)
wizard.happy()
sleep(EMOTE_INTERVAL)
wizard.sad()
sleep(EMOTE_INTERVAL)
wizard.exit(1)

sleep(2)

wizard.enter(1)
print("Ahaha, I'll give you another try!")
sleep(1)
wizard.happy()
sleep(EMOTE_INTERVAL // 2)