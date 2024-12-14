class StringVar():
    def __init__(self, string):
        self._string = string
        
    def set(self, string):
        self._string = string
    
    def get(self):
        return self._string
    
obj = StringVar('ооо')
print(obj.get())
obj.set('оао')
print(obj.get())