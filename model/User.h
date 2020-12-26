//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_USER_H
#define PROJECT_USER_H


#include "Role.h"
#include "Settings.h"

class User : public StoredModel{
public:
    User(char *firstName, char *lastName, char *email, char *password, Role *role, Settings *settings);

private:
    char* first_name;
public:
    char *getFirstName() const;

    void setFirstName(char *firstName);

    char *getLastName() const;

    void setLastName(char *lastName);

    char *getEmail() const;

    void setEmail(char *email);

    char *getPassword() const;

    void setPassword(char *password);

    Role *getRole() const;

    void setRole(Role *role);

    Settings *getSettings() const;

    void setSettings(Settings *settings);

private:
    char* last_name;
    char* email;
    char* password;
    Role* role;
    Settings* settings;

};


#endif //PROJECT_USER_H
