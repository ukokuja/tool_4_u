//
// Created by Lucas Kujawski on 26/12/2020.
//

#include "User.h"

char *User::getFirstName() const {
    return first_name;
}

void User::setFirstName(char *firstName) {
    first_name = firstName;
}

char *User::getLastName() const {
    return last_name;
}

void User::setLastName(char *lastName) {
    last_name = lastName;
}

char *User::getEmail() const {
    return email;
}

void User::setEmail(char *email) {
    User::email = email;
}

char *User::getPassword() const {
    return password;
}

void User::setPassword(char *password) {
    User::password = password;
}

Role *User::getRole() const {
    return role;
}

void User::setRole(Role *role) {
    User::role = role;
}

Settings *User::getSettings() const {
    return settings;
}

void User::setSettings(Settings *settings) {
    User::settings = settings;
}

User::User(char *firstName, char *lastName, char *email, char *password, Role *role, Settings *settings) : first_name(
        firstName), last_name(lastName), email(email), password(password), role(role), settings(settings) {}
