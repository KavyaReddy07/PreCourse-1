class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data)
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = ListNode(data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """

        curr = self.head
        # prev = ListNode(-1)
        # prev.next = curr
        while curr and curr.data != key:
            # prev = curr
            curr = curr.next
        if not curr:
            return None
        return curr.data
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """

        curr = self.head
        prev = ListNode(-1)
        prev.next = curr
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr and curr.data == key:
            prev.next = curr.next


