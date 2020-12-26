//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_STOREDMODEL_H
#define PROJECT_STOREDMODEL_H


class StoredModel {
    int id;
    virtual void load(char**)=0;
    virtual void save(char**)=0;
};


#endif //PROJECT_STOREDMODEL_H
