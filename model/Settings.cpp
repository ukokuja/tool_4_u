//
// Created by Lucas Kujawski on 26/12/2020.
//

#include "Settings.h"

char *Settings::getKey() const {
    return key;
}

void Settings::setKey(char *key) {
    Settings::key = key;
}

char *Settings::getValue() const {
    return value;
}

void Settings::setValue(char *value) {
    Settings::value = value;
}
