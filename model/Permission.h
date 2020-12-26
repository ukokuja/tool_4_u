//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_PERMISSION_H
#define PROJECT_PERMISSION_H


#include "StoredModel.h"

class Permission : public StoredModel {

    char** allowed_actions;
public:
    char **getAllowedActions() const;

    void addAllowedAction(char *allowedAction);

    void removeAllowedAction(char *allowedAction);
};


#endif //PROJECT_PERMISSION_H
