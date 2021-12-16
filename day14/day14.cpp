#include <iostream>
#include <fstream>
#include <string>
#include <vector>

// Linked list version of a polynmer
class PolymerElement {
    public:
        char element;
        PolymerElement *nextElement;
        PolymerElement(char element, PolymerElement *nextElement) {
            this->element       = element;
            this->nextElement   = nextElement;
        }
};

class Polymer {
    public:
        PolymerElement *head;
        Polymer(PolymerElement *head) {
            this->head = head;
        }

        void print() {
            PolymerElement *currElement = head;
            while(currElement != NULL) {
                std::cout << currElement->element;
                currElement = currElement->nextElement;
            }
        }
};

// Input parser
Polymer* inputParser(std::string filename) {
    // Read the file
    std::vector<std::string> lines;
    std::fstream file;
    file.open(filename, std::ios::in);
    if(file.is_open()) {
        std::string line;
        while(getline(file, line)){
            lines.push_back(line);
        }
        file.close();
    }

    // Create the polymer from the template
    PolymerElement *head = new PolymerElement(lines[0][0], NULL);
    PolymerElement *currElement = head;
    for(int i = 0; i < lines[0].length(); i++) {
        PolymerElement *element = new PolymerElement(lines[0][i], NULL);
        currElement->nextElement = element;
        currElement = element;
    }

    return new Polymer(head);
}

int main() {
    Polymer *polymer = inputParser("example1");
    polymer->print();
    return 0;
}