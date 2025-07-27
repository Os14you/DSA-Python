from scattered.LinkedList import LinkedList

def test_linked_list():
    ll = LinkedList()
    ll.insert_front(1)
    ll.insert_front(2)
    ll.insert_front(3)
    ll.insert_end(4)

    assert ll.get(0) == 3
    assert ll.get(1) == 2
    assert ll.get(2) == 1
    assert ll.get(3) == 4

    ll.delete_front()
    assert ll.get(0) == 2
    assert ll.get(1) == 1
    assert ll.get(2) == 4

    ll.delete_end()
    assert ll.get(0) == 2
    assert ll.get(1) == 1

    ll.delete(1)
    assert ll.get(0) == 2

    print("All tests passed!")


def main():
    test_linked_list()

if __name__ == "__main__":
    main()