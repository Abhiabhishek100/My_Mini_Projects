import  time
from winotify import Notification, audio
toast= Notification(app_id="neuralline script", title="message title",msg="hello world!",duration="long",icon="F:\me.Jpg")
toast.set_audio(audio.LoopingAlarm, loop=True)
toast.add_actions(label="click",launch="https://youtube.com/")

toast.show()