//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_SETTINGS_H
#define PROJECT_SETTINGS_H


#include "StoredModel.h"

class Settings : public StoredModel {
    char* key;
public:
    char *getKey() const;

    void setKey(char *key);

    char *getValue() const;

    void setValue(char *value);

private:
    char* value;
};


#endif //PROJECT_SETTINGS_H
