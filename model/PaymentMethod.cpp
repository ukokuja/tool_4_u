//
// Created by Lucas Kujawski on 26/12/2020.
//

#include "PaymentMethod.h"

char *PaymentMethod::getName() const {
    return name;
}

void PaymentMethod::setName(char *name) {
    PaymentMethod::name = name;
}
