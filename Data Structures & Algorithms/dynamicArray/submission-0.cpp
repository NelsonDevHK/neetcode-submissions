class DynamicArray {
public:
    int capacity;
    int size;
    vector<int> v;

    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        v.resize(capacity);  // allocate size elements initialized to 0
    }

    int get(int i) {
        if (i < 0 || i >= size) {
            throw out_of_range("Index out of range");
        }
        return v[i];
    }

    void set(int i, int n) {
        if (i < 0 || i >= size) {
            throw out_of_range("Index out of range");
        }
        v[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        v[size++] = n;
    }

    int popback() {
        if (size == 0) {
            throw out_of_range("Pop from empty array");
        }
        return v[--size];
    }

    void resize() {
        capacity *= 2;
        vector<int> new_v(capacity);
        for (int i = 0; i < size; i++) {
            new_v[i] = v[i];
        }
        v = move(new_v);
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
