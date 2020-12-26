//
// Created by Lucas Kujawski on 26/12/2020.
//

#include "Client.h"

Plan *Client::getPlan() const {
    return plan;
}

void Client::setPlan(Plan *plan) {
    Client::plan = plan;
}

char *Client::getPhoneNumber() const {
    return phone_number;
}

void Client::setPhoneNumber(char *phoneNumber) {
    phone_number = phoneNumber;
}

PaymentMethod *Client::getPaymentMethod() const {
    return paymentMethod;
}

void Client::setPaymentMethod(PaymentMethod *paymentMethod) {
    Client::paymentMethod = paymentMethod;
}
