class ObjectStack<T> {
  private count = 0;
  private storage: { [key: number]: T } = {};

  push(item: T): void {
    this.storage[this.count] = item;
    this.count++;
  }

  pop(): T | undefined {
    if (this.count === 0) return undefined;

    const lastElem = this.storage[this.count - 1];
    delete this.storage[this.count - 1];
    this.count--;
    return lastElem;
  }

  get size(): number {
    return this.count;
  }

  peek(): T | undefined {
    if (this.count === 0) return undefined;
    return this.storage[this.count - 1];
  }
}

const stack = new ObjectStack<number>();

stack.push(10);
stack.push(20);
stack.push(30);

console.log(stack.size); // 3
console.log(stack.peek()); // 30
console.log(stack.pop());  // 30
console.log(stack.peek()); // 20
console.log(stack.size); // 2
console.log(stack.pop());  // 20
console.log(stack.pop());  // 10
console.log(stack.pop());  // undefined
