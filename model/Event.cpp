//
// Created by Lucas Kujawski on 27/12/2020.
//

#include "Event.h"

Event::Event(int timestamp, char *category, char *action, char *label, Client *client) : timestamp(timestamp),
                                                                                         category(category),
                                                                                         action(action), label(label),
                                                                                         client(client) {}
