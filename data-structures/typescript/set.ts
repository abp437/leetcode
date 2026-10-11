class MySet<T> {
  #items: T[] = [];

  #getIndex(item: T): number {
    return this.#items.indexOf(item);
  }

  #uncheckedAdd(item: T): void {
    this.#items.push(item);
  }

  has(item: T): boolean {
    return this.#getIndex(item) > -1;
  }

  values(): readonly T[] {
    return [...this.#items];
  }

  add(item: T): void {
    if (this.has(item)) return;
    this.#items.push(item);
  }

  remove(item: T): T | undefined {
    const index = this.#getIndex(item);

    if (index > -1) {
      this.#items.splice(index, 1);
      return item;
    }

    return undefined;
  }

  union(argSet: MySet<T>): MySet<T> {
    const unionSet = new MySet<T>();

    this.values().forEach((val: T) => {
      unionSet.#uncheckedAdd(val);
    });

    argSet.values().forEach((val: T) => {
      unionSet.add(val);
    });

    return unionSet;
  }

  intersection(argSet: MySet<T>): MySet<T> {
    const intersectionSet = new MySet<T>();

    argSet.values().forEach((val: T) => {
      if (this.has(val)) {
        intersectionSet.#uncheckedAdd(val);
      }
    });

    return intersectionSet;
  }

  difference(argSet: MySet<T>): MySet<T> {
    const differenceSet = new MySet<T>();

    this.values().forEach((val: T) => {
      if (!argSet.has(val)) {
        differenceSet.#uncheckedAdd(val);
      }
    });

    return differenceSet;
  }

  isSubsetOf(argSet: MySet<T>): boolean {
    return this.values().every((val: T) => argSet.has(val));
  }

  get size(): number {
    return this.#items.length;
  }
}

const setA = new MySet<number>();

setA.add(1);
setA.add(2);
setA.add(3);

const setB = new MySet<number>();

setB.add(2);
setB.add(3);
setB.add(4);

// Basic operations
console.log(setA.size); // 3
console.log(setA.has(2)); // true
console.log(setA.has(4)); // false
console.log(setA.values()); // [1, 2, 3]

// Adding duplicates
setA.add(2);
console.log(setA.size); // 3

// Removing elements
console.log(setA.remove(2)); // 2
console.log(setA.remove(5)); // undefined
console.log(setA.values()); // [1, 3]
console.log(setA.size); // 2

// Union
console.log(setA.union(setB).values()); // [1, 3, 2, 4]

// Intersection
console.log(setA.intersection(setB).values()); // [3]

// Difference
console.log(setA.difference(setB).values()); // [1]

// isSubsetOf
const setC = new MySet<number>();
setC.add(1);
setC.add(3);

console.log(setC.isSubsetOf(setA)); // true
console.log(setA.isSubsetOf(setB)); // false

// Empty set
const emptySet = new MySet<number>();
console.log(emptySet.size); // 0
console.log(emptySet.isSubsetOf(setA)); // true
console.log(emptySet.remove(1)); // undefined
