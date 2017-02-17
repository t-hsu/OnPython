#define own main function
def main():
	cough(3)
	sneeze(3)
#define cough function
def cough(n):
	say("cough", n)
#define sneeze function
def sneeze(n):
	say("achoo", n)
#define say function which takes in a loop(range) and print output
def say(word, n):
	for i in range(n):
		print("{}".format(word))
#main has to be called in order for this program to work
if __name__ == "__main__":
    main()
