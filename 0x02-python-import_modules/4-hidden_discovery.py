#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    n = dir(hidden_4)
    for nm in n:
        if nm[:2] != "__":
            print(nm)
