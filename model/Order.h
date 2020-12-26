//
// Created by Lucas Kujawski on 27/12/2020.
//

#ifndef PROJECT_ORDER_H
#define PROJECT_ORDER_H


#include "StoredModel.h"
#include "Item.h"
#include "Client.h"

class Order : public StoredModel {
    Item* item;
public:
    Item *getItem() const;

    Client *getClient() const;

    int getStartDate() const;

    int getEndDate() const;

public:
    Order(Item *item, Client *client, int startDate);

private:
    Client* client;
    int start_date;
    int end_date;
public:
    void setEndDate(int endDate);
};


#endif //PROJECT_ORDER_H
