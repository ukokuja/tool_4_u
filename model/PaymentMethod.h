//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_PAYMENTMETHOD_H
#define PROJECT_PAYMENTMETHOD_H


class PaymentMethod {

    char* name;
public:
    char *getName() const;

    void setName(char *name);
};


#endif //PROJECT_PAYMENTMETHOD_H
