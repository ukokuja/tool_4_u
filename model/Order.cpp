//
// Created by Lucas Kujawski on 27/12/2020.
//

#include "Order.h"

Order::Order(Item *item, Client *client, int startDate) : item(item), client(client), start_date(startDate) {}

void Order::setEndDate(int endDate) {
    end_date = endDate;
}

Item *Order::getItem() const {
    return item;
}

Client *Order::getClient() const {
    return client;
}

int Order::getStartDate() const {
    return start_date;
}

int Order::getEndDate() const {
    return end_date;
}
