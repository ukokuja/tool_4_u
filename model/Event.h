//
// Created by Lucas Kujawski on 27/12/2020.
//

#ifndef PROJECT_EVENT_H
#define PROJECT_EVENT_H


#include "StoredModel.h"
#include "Client.h"

class Event : public StoredModel {
public:
    Event(int timestamp, char *category, char *action, char *label, Client *client);

private:

    int timestamp;
    char* category;
    char* action;
    char* label;
    Client* client;
};


#endif //PROJECT_EVENT_H
