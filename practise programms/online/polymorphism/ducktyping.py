class pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class editor:
    def execute(self):
        print("Spell check")
        print("convention check")

class laptop:
    def code(self,ide):
        ide.execute()

ide=editor()
lap1=laptop()
lap1.code(ide)
    
