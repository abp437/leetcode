class Queue<T> {
  #items: { [key: number]: T } = {};
  #head: number = 0;
  #tail: number = 0;

  enqueue(item: T): void {
    this.#items[this.#tail] = item;
    this.#tail++;
  }

  dequeue(): T | undefined {
    if (this.isEmpty) return undefined;

    const lastItem = this.#items[this.#head];
    delete this.#items[this.#head];

    this.#head++;

    return lastItem;
  }

  toArray(): T[] {
    return Object.values(this.#items);
  }

  get isEmpty(): boolean {
    return this.#head === this.#tail;
  }

  get front(): T | undefined {
    return this.#items[this.#head];
  }

  get size(): number {
    return this.#tail - this.#head;
  }
}

// Example usage
const queue = new Queue<number>();

// Test initial state
console.log("Initial queue:", queue.toArray());
console.log("Is empty:", queue.isEmpty);
console.log("Queue size:", queue.size);
console.log("Front item:", queue.front);

// Test enqueue
console.log("Enqueue 42");
queue.enqueue(42);
console.log("Current queue:", queue.toArray());
console.log("Is empty:", queue.isEmpty);
console.log("Front item:", queue.front);
console.log("Queue size:", queue.size);

console.log("Enqueue 17");
queue.enqueue(17);
console.log("Current queue:", queue.toArray());
console.log("Front item:", queue.front);
console.log("Queue size:", queue.size);

console.log("Enqueue 89");
queue.enqueue(89);
console.log("Current queue:", queue.toArray());
console.log("Front item:", queue.front);
console.log("Queue size:", queue.size);

// Test dequeue
console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());
console.log("Front item:", queue.front);
console.log("Queue size:", queue.size);
console.log("Is empty:", queue.isEmpty);

// Enqueue after dequeue
console.log("Enqueue 63");
queue.enqueue(63);
console.log("Current queue:", queue.toArray());

console.log("Enqueue 28");
queue.enqueue(28);
console.log("Current queue:", queue.toArray());
console.log("Front item:", queue.front);
console.log("Queue size:", queue.size);

// Dequeue multiple items
console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());

console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());
console.log("Front item:", queue.front);
console.log("Queue size:", queue.size);

// Test more enqueues
console.log("Enqueue 95");
queue.enqueue(95);

console.log("Enqueue 11");
queue.enqueue(11);

console.log("Current queue:", queue.toArray());
console.log("Front item:", queue.front);
console.log("Queue size:", queue.size);
console.log("Is empty:", queue.isEmpty);

// Continue dequeuing and enqueueing
console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());

console.log("Enqueue 74");
queue.enqueue(74);
console.log("Current queue:", queue.toArray());

console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());
console.log("Front item:", queue.front);

console.log("Enqueue 36");
queue.enqueue(36);
console.log("Current queue:", queue.toArray());
console.log("Queue size:", queue.size);

// Drain the queue
console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());

console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());

console.log("Dequeued:", queue.dequeue());
console.log("Current queue:", queue.toArray());

// Test empty queue behavior
console.log("Is empty:", queue.isEmpty);
console.log("Queue size:", queue.size);
console.log("Front item:", queue.front);
console.log("Dequeue from empty queue:", queue.dequeue());
console.log("Final queue:", queue.toArray());
console.log("Final queue size:", queue.size);
console.log("Is empty:", queue.isEmpty);
