

from datastructures.bag import Bag


def main():

    bag = Bag[int]()

    
    bag.add(12)
    bag.add(13)
    bag.clear()
    print(12 in bag)
  
    
if __name__ == '__main__':
    main()
