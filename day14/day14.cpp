#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <array>
#include <map>

// Linked list version of a polynmer
class PolymerElement {
    public:
        char            element;
        PolymerElement  *nextElement;

        PolymerElement(char element, PolymerElement *nextElement) {
            this->element       = element;
            this->nextElement   = nextElement;
        }
};

class Polymer {
    public:
        PolymerElement  *head;
        PolymerElement  *tail;
        uint64_t        length;

        Polymer(PolymerElement *head, PolymerElement *tail, int length) {
            this->head      = head;
            this->tail      = tail;
            this->length    = length;
        }

        void print() {
            PolymerElement *currElement = head;
            while(currElement != NULL) {
                std::cout << currElement->element;
                currElement = currElement->nextElement;
            }
            std::cout << "\n";
        }

        void addElement(PolymerElement *currElement, PolymerElement *newElement)
        {
            PolymerElement *nextElement = currElement->nextElement;
            currElement->nextElement    = newElement;
            newElement->nextElement     = nextElement;
            this->length++;
            if(currElement == this->tail)
            {
                this->tail = newElement;
            }
        }
};

// Input parser
Polymer* inputParser(std::string filename, std::vector<std::array<char, 3>> &rules) {
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
    int length = 1;
    for(int i = 1; i < lines[0].length(); i++) {
        PolymerElement *element = new PolymerElement(lines[0][i], NULL);
        currElement->nextElement = element;
        currElement = element;
        length++;
    }
    Polymer *polymer = new Polymer(head, currElement, length);

    // Fill in the list of rules
    for(int i = 2; i < lines.size(); i++) {
        std::array<char, 3> rule;
        rule[0] = lines[i][0];
        rule[1] = lines[i][1];
        rule[2] = lines[i][6];
        rules.push_back(rule);
    }

    return polymer;
}

int main() {
    // Read the file
    std::vector<std::array<char, 3>> rules;
    Polymer *polymer = inputParser("example1", rules);
   
    // Apply the rule 40 times
    for(int i = 0; i < 40; i++) {
        PolymerElement *currElement = polymer->head;
        while(currElement != polymer->tail) {
            for(int j = 0; j < rules.size(); j++) {
                if(currElement->element == rules[j][0] && currElement->nextElement->element == rules[j][1]) {
                    polymer->addElement(currElement, new PolymerElement(rules[j][2], NULL));
                    currElement = currElement->nextElement;
                    break;
                }
            }
            currElement = currElement->nextElement;
        }

        std::cout << i;
        std::cout << "\n";
    }

    // Count the number of each element
    std::map<char, uint64_t> numOccuurances;
    PolymerElement *currElement = polymer->head;
    while(currElement != NULL) {
        if(numOccuurances.find(currElement->element) == numOccuurances.end()) {
            numOccuurances.insert(std::make_pair(currElement->element, 1));
        }
        else {
            uint64_t prevOcc = numOccuurances[currElement->element];
            numOccuurances[currElement->element] = prevOcc + 1;
        }
        currElement = currElement->nextElement;
    }

    // Find the number of occurances that is most and least common
    uint64_t mostCommonOcc = 0;
    uint64_t leastCommonOcc = -1;
    std::map<char, uint64_t>::iterator mapIterator;
    for(mapIterator = numOccuurances.begin(); mapIterator != numOccuurances.end(); mapIterator++) {
        if(mapIterator->second > mostCommonOcc) {
            mostCommonOcc = mapIterator->second;
        }
        if(mapIterator->second < leastCommonOcc) {
            leastCommonOcc = mapIterator->second;
        }
    }

    // Print result
    std::cout << mostCommonOcc - leastCommonOcc;

    return 0;
}