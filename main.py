import keys
import  time
import os

def save_data(time,path):
        with open(path,"a") as f:
            f.write(str(time)+'\n')
        f.close()


if __name__ == "__main__":
    DATA_SET_NAME = "DATASET_2024"
    Mode = "COLLECT"
    COUNT_DOWN= 8
    ACTION_NAME = "punch"
    INDEX = 2
    DURATION = 4
    NUM_ACTIONS = 20
    keys = keys.Keys()
    pathname = rf"{DATA_SET_NAME}/{INDEX}/{ACTION_NAME}/time-data.txt"
    if os.path.exists(pathname):
        raise ValueError("文件已存在，请重新命名保存文件！")
    else:
        os.makedirs(os.path.dirname(pathname), exist_ok=True)

    for i in [_ for _ in range(1,COUNT_DOWN + 1)][::-1]:
        print(i)
        time.sleep(1)

    if Mode == "COLLECT":
        for i in range(NUM_ACTIONS):
            print(f"======= Start Epoch {i+1}/{NUM_ACTIONS} NOW =======")
            keys.directKey("s")
            save_data(rf"{time.time()},action",pathname)
            for _ in [i for i in range(1,DURATION+1)][::-1]:
                print(_)
                time.sleep(1)
            print("======== SWITCH TO IDLE ! ========")
            keys.directKey("s",keys.key_release)
            save_data(rf"{time.time()},idle",pathname)
            for _ in [i for i in range(1,DURATION+1)][::-1]:
                print(_)
                time.sleep(1)

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