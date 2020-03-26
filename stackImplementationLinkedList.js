class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    // View the very top node
    peek() {
        return this.top
        
    }

    // Add node to the top of the stack
    push(value) {
        let newNode = new Node(value)

        if (this.length === 0) {
            this.bottom = newNode;
            this.top = newNode;
        } else {
            // const holdingPointer = this.top;
            // this.top = newNode
            // this.top.next = holdingPointer;

            newNode.next = this.top
            this.top = newNode
        }

        //increment by one
        this.length++;

        //return the linked list
        return this;
    }

    // Remove node from the top of the stack
    pop() {
        if (this.isEmpty()) {
            return this;
        }

        if (this.length === 1) {
            this.bottom = null;
        }

        const oldTop = this.top;
        const newTop = this.top.next;
        this.top = newTop;
        this.length--;
        return oldTop;
    }

    //implement isEmpty method to check if the stack is empty
    isEmpty() {
        return this.length === 0
    }
}


const myStack = new Stack();