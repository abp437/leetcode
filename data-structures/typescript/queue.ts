class Queue<T> {
  private items: { [key: number]: T } = {};
  private head = 0;
  private tail = 0;
  private length = 0;

  enqueue(item: T): void {
    this.items[this.tail] = item;
    this.tail++;
    this.length++;
  }

  dequeue(): T | undefined {
    if (this.length === 0) {
      return undefined;
    }

    const lastItem = this.items[this.head];
    delete this.items[this.head];

    this.head++;
    this.length--;

    return lastItem;
  }

  get size(): number {
    return this.length;
  }

  get contents(): T[] {
    return Object.values(this.items);
  }
}

// Example usage
const queue = new Queue<number>();

console.log("Initial queue:", queue.contents);
console.log("Enqueue 42");
queue.enqueue(42);

console.log("Enqueue 17");
queue.enqueue(17);

console.log("Enqueue 89");
queue.enqueue(89);

console.log("Current queue:", queue.contents);
console.log("Queue size:", queue.size);

console.log("Dequeued:", queue.dequeue());

console.log("Enqueue 63");
queue.enqueue(63);

console.log("Enqueue 28");
queue.enqueue(28);

console.log("Current queue:", queue.contents);

console.log("Dequeued:", queue.dequeue());
console.log("Dequeued:", queue.dequeue());

console.log("Enqueue 95");
queue.enqueue(95);

console.log("Enqueue 11");
queue.enqueue(11);

console.log("Current queue:", queue.contents);
console.log("Queue size:", queue.size);

console.log("Dequeued:", queue.dequeue());

console.log("Enqueue 74");
queue.enqueue(74);

console.log("Dequeued:", queue.dequeue());

console.log("Enqueue 36");
queue.enqueue(36);

console.log("Current queue:", queue.contents);

console.log("Dequeued:", queue.dequeue());
console.log("Dequeued:", queue.dequeue());

console.log("Final queue:", queue.contents);
console.log("Final queue size:", queue.size);
