class ConsoleUI:
    def display(self, status):
        os.system('clear')
        for eid, info in status.items():
            print(f"电梯{eid}: [{info['current']}] 方向:{'▲' if info['direction']==1 else '▼' if info['direction']==-1 else '·'}")
            print(f"目标楼层: {info['targets']} 门状态: {'开' if info['door_open'] else '关'}")

    def get_input(self):
        return input("输入请求 (格式：楼层,方向 例：5,up)：")