//
// Created by Lucas Kujawski on 26/12/2020.
//

#ifndef PROJECT_PLAN_H
#define PROJECT_PLAN_H


#include "StoredModel.h"

class Plan : public StoredModel {

    int price_per_month;
public:
    int getPricePerMonth() const;

    void setPricePerMonth(int pricePerMonth);

    int getAllowedItemsPerMonth() const;

    void setAllowedItemsPerMonth(int allowedItemsPerMonth);

private:
    int allowed_items_per_month;
};


#endif //PROJECT_PLAN_H
