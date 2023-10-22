from data_structures.queue import Queue


class Dog:
    """
    Dog class
    """
    species='dog'
    def __init__(self,name:str=None):
        self.name=name

class Cat:
    """
    Cat class
    """
    species='cat'
    def __init__(self,name:str=None):
        self.name=name

class AnimalShelter:
    """
    Implements a que(FIFO) of dogs and cats held at animal shelter.
    """
    def __init__(self):
        """
        On initialization, a queue component is created to handle primary que.
        Also, temporary queue component created to recycle animal instances through to primary que to maintain order of que.
        """
        self.queue = Queue()
        self.queue_temp = Queue()

    def enqueue(self,animal):
        """
        So long as argument is a cat or dog instance, with be enqueued at back.
        """
        if isinstance(animal,Dog) or isinstance(animal,Cat):
            self.queue.enqueue(animal)
        else:
            raise TypeError("Can only add Cat or Dog class instances to AnimalShelter que.")

    def dequeue(self,prefer:str=None) -> Dog or Cat or None:
        """
        Dequeues from animal shelter que.
        If no preference made and que isn't empty, will dequeue first animal and return.
        If preference not cat or dog, will return None.
        Otherwise, will return first cat or dog instance based on preference provided.
        """
        # if no preference is made
        if prefer is None:
            return self.queue.dequeue() # will handle exception if empty

        # if preference is made for cat or dog
        elif prefer=="dog" or prefer=='cat':
            node_return = None

            # if first animal instance matches preference
            if not self.queue.is_empty():
                node_front = self.queue.peek()
                # check first animal instance, return if matches
                if node_front.species == prefer:
                    self.queue.dequeue()
                    return node_front
                # traverse one
                else:
                    self.queue_temp.enqueue(self.queue.dequeue())
            # if que is empty
            else:
                return node_return

            # remove and check remainder of animal instance in the primary que
            bool_found_preferred = False
            while not self.queue.is_empty():
                node_curr = self.queue.dequeue()
                # if preferred animal instance found, save separately
                if node_curr.species == prefer and bool_found_preferred==False:
                    node_return = node_curr
                    bool_found_preferred = True
                # for all other instances add to temporary que
                else:
                    self.queue_temp.enqueue(node_curr)

            # maintain order of que by converting temporary to primary que
            self.queue = self.queue_temp
            self.queue_temp = Queue()

            # return preferred animal instance if found in traversal or None otherwise
            return node_return

        # if unintelligible preference
        else:
            return None

