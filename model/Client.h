//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_CLIENT_H
#define PROJECT_CLIENT_H


#include "User.h"
#include "Plan.h"
#include "PaymentMethod.h"

class Client : public User {

    Plan* plan;
public:
    Plan *getPlan() const;

    void setPlan(Plan *plan);

    char *getPhoneNumber() const;

    void setPhoneNumber(char *phoneNumber);

    PaymentMethod *getPaymentMethod() const;

    void setPaymentMethod(PaymentMethod *paymentMethod);

private:
    char* phone_number;
    PaymentMethod* paymentMethod;
};


#endif //PROJECT_CLIENT_H
