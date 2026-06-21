from __future__ import annotations

from typing import Callable, Iterator, Optional, TypeVar

T = TypeVar("T")


class DynamicArray:
    """Mang dong tu cai dat cho cac danh sach nghiep vu."""

    def __init__(self, capacity: int = 4) -> None:
        if capacity <= 0:
            capacity = 4
        self._capacity = capacity
        self._size = 0
        self._data = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        index = 0
        while index < self._size:
            yield self._data[index]
            index += 1

    def is_empty(self) -> bool:
        return self._size == 0

    def append(self, value: T) -> None:
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def get(self, index: int) -> T:
        self._validate_index(index)
        return self._data[index]

    def set(self, index: int, value: T) -> None:
        self._validate_index(index)
        self._data[index] = value

    def insert(self, index: int, value: T) -> None:
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        i = self._size
        while i > index:
            self._data[i] = self._data[i - 1]
            i -= 1
        self._data[index] = value
        self._size += 1

    def remove_at(self, index: int) -> T:
        self._validate_index(index)
        removed = self._data[index]
        i = index
        while i < self._size - 1:
            self._data[i] = self._data[i + 1]
            i += 1
        self._size -= 1
        self._data[self._size] = None
        if self._capacity > 4 and self._size <= self._capacity // 4:
            self._resize(max(4, self._capacity // 2))
        return removed

    def clear(self) -> None:
        self._capacity = 4
        self._size = 0
        self._data = [None] * self._capacity

    def copy(self) -> "DynamicArray":
        result = DynamicArray(self._capacity)
        for value in self:
            result.append(value)
        return result

    def find_index(self, predicate: Callable[[T], bool]) -> int:
        index = 0
        while index < self._size:
            if predicate(self._data[index]):
                return index
            index += 1
        return -1

    def _resize(self, new_capacity: int) -> None:
        new_data = [None] * new_capacity
        i = 0
        while i < self._size:
            new_data[i] = self._data[i]
            i += 1
        self._data = new_data
        self._capacity = new_capacity

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")


class _Entry:
    def __init__(self, key: str, value: object) -> None:
        self.key = key
        self.value = value
        self.next: Optional["_Entry"] = None


class LinkedList:
    """Danh sach lien ket don dung lam bucket cua bang bam."""

    def __init__(self) -> None:
        self.head: Optional[_Entry] = None

    def put(self, key: str, value: object) -> bool:
        current = self.head
        while current is not None:
            if current.key == key:
                current.value = value
                return False
            current = current.next
        node = _Entry(key, value)
        node.next = self.head
        self.head = node
        return True

    def get(self, key: str) -> object | None:
        current = self.head
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key: str) -> bool:
        current = self.head
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def items(self) -> DynamicArray:
        result = DynamicArray()
        current = self.head
        while current is not None:
            result.append((current.key, current.value))
            current = current.next
        return result


class HashTable:
    """Bang bam separate chaining voi ham bam chuoi tu cai dat."""

    def __init__(self, capacity: int = 101) -> None:
        if capacity < 11:
            capacity = 11
        self._capacity = capacity
        self._size = 0
        self._buckets = [None] * self._capacity
        index = 0
        while index < self._capacity:
            self._buckets[index] = LinkedList()
            index += 1

    def __len__(self) -> int:
        return self._size

    def put(self, key: str, value: object) -> None:
        normalized = self._normalize_key(key)
        bucket = self._buckets[self._hash(normalized)]
        inserted = bucket.put(normalized, value)
        if inserted:
            self._size += 1

    def get(self, key: str) -> object | None:
        normalized = self._normalize_key(key)
        return self._buckets[self._hash(normalized)].get(normalized)

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def remove(self, key: str) -> bool:
        normalized = self._normalize_key(key)
        removed = self._buckets[self._hash(normalized)].remove(normalized)
        if removed:
            self._size -= 1
        return removed

    def values(self) -> DynamicArray:
        result = DynamicArray()
        index = 0
        while index < self._capacity:
            for _, value in self._buckets[index].items():
                result.append(value)
            index += 1
        return result

    def items(self) -> DynamicArray:
        result = DynamicArray()
        index = 0
        while index < self._capacity:
            for item in self._buckets[index].items():
                result.append(item)
            index += 1
        return result

    def clear(self) -> None:
        index = 0
        while index < self._capacity:
            self._buckets[index] = LinkedList()
            index += 1
        self._size = 0

    def _hash(self, key: str) -> int:
        value = 0
        for ch in key:
            value = (value * 31 + ord(ch)) % self._capacity
        return value

    def _normalize_key(self, key: str) -> str:
        return str(key).strip().upper()


def linear_search(array: DynamicArray, predicate: Callable[[T], bool]) -> DynamicArray:
    result = DynamicArray()
    for value in array:
        if predicate(value):
            result.append(value)
    return result


def quick_sort(array: DynamicArray, key: Callable[[T], object], reverse: bool = False) -> None:
    if len(array) <= 1:
        return
    _quick_sort_range(array, 0, len(array) - 1, key, reverse)


def _quick_sort_range(
    array: DynamicArray,
    left: int,
    right: int,
    key: Callable[[T], object],
    reverse: bool,
) -> None:
    if left >= right:
        return
    pivot_index = _partition(array, left, right, key, reverse)
    _quick_sort_range(array, left, pivot_index - 1, key, reverse)
    _quick_sort_range(array, pivot_index + 1, right, key, reverse)


def _partition(
    array: DynamicArray,
    left: int,
    right: int,
    key: Callable[[T], object],
    reverse: bool,
) -> int:
    pivot = key(array.get(right))
    i = left - 1
    j = left
    while j < right:
        current_key = key(array.get(j))
        should_swap = current_key >= pivot if reverse else current_key <= pivot
        if should_swap:
            i += 1
            _swap(array, i, j)
        j += 1
    _swap(array, i + 1, right)
    return i + 1


def _swap(array: DynamicArray, i: int, j: int) -> None:
    if i == j:
        return
    temp = array.get(i)
    array.set(i, array.get(j))
    array.set(j, temp)

