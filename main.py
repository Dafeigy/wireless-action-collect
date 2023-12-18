import keys
import  time
import os
class Agent():
    def __init__(self,keys:keys.Keys) -> None:
        self.state = "idle"
        self.action_dict = {
            "idle":"",
            "left":self.left,
            "right":self.right,
            "down":self.down,
            "jump":self.jump,
            "punch":self.punch,
            "kick":self.kick
        }
        self.keys = keys

    def left(self):
        self.keys.directKey("a")
        self.state = "left"

    def right(self):
        self.keys.directKey("d")
        self.state = "right"

    def down(self):
        self.keys.directKey("s")
        self.state = "down"

    def jump(self):
        self.keys.directKey("w")
        self.state = "jump"
        time.sleep(0.01)
        self.keys.directKey("w",keys.key_release)
        self.state = "idle"

    def punch(self):
        self.keys.directKey("i")
        self.state = "punch"
        time.sleep(0.002)
        self.keys.directKey("i",keys.key_release)
        self.state = "idle"


    def kick(self):
        self.keys.directKey("k")
        self.state = "kick"
        time.sleep(0.002)
        self.keys.directKey("k",keys.key_release)
        self.state = "idle"

    def release(self,prev_state):
        if prev_state == "idle":
            pass
        else:
            keys.directKey(self.action_dict[prev_state], keys.key_release)
            self.state = "idle"
def save_data(time,path):
        with open(path,"a") as f:
            f.write(str(time)+'\n')
        f.close()
if __name__ == "__main__":
    Mode = "COLLECT"
    COUNT_DOWN= 8
    ACTION_NAME = "punch"
    INDEX = 1
    DURATION = 2
    NUM_ACTIONS = 10
    keys = keys.Keys()
    pathname = rf"NEWdata/{INDEX}/{ACTION_NAME}/time-data.txt"
    if os.path.exists(pathname):
        raise ValueError("文件已存在，请重新命名保存文件！")
    else:
        os.makedirs(os.path.dirname(pathname), exist_ok=True)

    for i in [i for i in range(1,COUNT_DOWN + 1)][::-1]:
        print(i)
        time.sleep(1)
    if Mode == "COLLECT":
        for i in range(NUM_ACTIONS):
            keys.directKey("s")
            save_data(time.time(),pathname)
            time.sleep(DURATION)
            keys.directKey("s",keys.key_release)
            save_data(time.time(),pathname)
            time.sleep(DURATION)

    if Mode == "TEST":
        keys.directKey("w")
        time.sleep(0.001)
        keys.directKey("w",keys.key_release)
        time.sleep(1)
        keys.directKey("w")
        time.sleep(0.001)
        keys.directKey("w",keys.key_release)
        time.sleep(2)

        
        keys.directKey("s")
        time.sleep(1)
        keys.directKey("s",keys.key_release)
        time.sleep(1)

        keys.directKey("s",type=keys.virtual_keys)
        time.sleep(1)
        keys.directKey("s",keys.key_release)
        time.sleep(1)

        keys.directKey("a",type=keys.virtual_keys)
        time.sleep(2)
        keys.directKey("a",keys.key_release)
        time.sleep(2)
    
        keys.directKey("d")
        time.sleep(2)
        keys.directKey("d",keys.key_release)
        time.sleep(2)

        keys.directKey("i")
        time.sleep(0.001)
        keys.directKey("i",keys.key_release)
        time.sleep(2)

        keys.directKey("i",type=keys.virtual_keys)
        time.sleep(0.001)
        keys.directKey("i",keys.key_release,type=keys.virtual_keys)
        time.sleep(2)

        keys.directKey("k")
        time.sleep(0.001)
        keys.directKey("k",keys.key_release)
        time.sleep(2)
        
        keys.directKey("k")
        time.sleep(0.001)
        keys.directKey("k",keys.key_release)
        time.sleep(2)