class PipTest(list):
    def __init__(self):
      pass
   
    def hello(self) -> None:
      print("Hello World!")
     #print("Hello World!")
      
      
def pipTest() -> None:
    p = PipTest()
    p.hello()

if __name__ == "__main__":
    pipTest()
  
__all__ = ['pipTest']
