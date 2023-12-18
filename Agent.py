import keys
import time
from concurrent.futures import ThreadPoolExecutor
person_number = 32
data_flag = "back"

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
        self.keys.directKey("w".keys.key_release)
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
    

if __name__ == "__main__":
    import os
    # Data collect timer Agent
    def save_data(time,path,name):
        with open(path+name+".txt","a") as f:
            f.write(str(time)+'\n')
        f.close()


    

    mas_path=rf'{str(person_number)}/'
    mas_collect_path=mas_path+str(data_flag)+'/'

    if os.path.exists(mas_path):
        if os.path.exists(mas_collect_path):
            print('请修改人员编号&动作编号！！')
            os._exit(0)
        else:
            os.makedirs(mas_collect_path)
    else:
        os.makedirs(mas_path)
        os.makedirs(mas_collect_path)
    
    threadpool=ThreadPoolExecutor(max_workers=16)
    keys = keys.Keys()
    agent = Agent(keys=keys)
    action = list(agent.action_dict.keys())
    for i in [i for i in range(1,9)][::-1]:
        print(i)
        time.sleep(1)
    for _ in range(10):
        threadpool.submit(save_data,f"{time.time()},down",mas_collect_path,'systime')
        # print(time.time())
        agent.down()
        time.sleep(4)
        threadpool.submit(save_data,f"{time.time()},idle",mas_collect_path,'systime')
        # print(time.time())
        keys.directKey("s", keys.key_release)
        time.sleep(4)
    threadpool.submit(save_data,f"{time.time()},finish",mas_collect_path,'systime')