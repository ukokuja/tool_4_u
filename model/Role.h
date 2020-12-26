//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_ROLE_H
#define PROJECT_ROLE_H


#include "StoredModel.h"
#include "Permission.h"

class Role : public StoredModel {
    Permission* permission_list;
public:
    Permission *getPermissionList() const;


    void addPermission(Permission *permission);

    void removePermission(Permission *permission);
};


#endif //PROJECT_ROLE_H
