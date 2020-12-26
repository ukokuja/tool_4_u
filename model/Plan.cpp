//
// Created by Lucas Kujawski on 26/12/2020.
//

#include "Plan.h"

int Plan::getPricePerMonth() const {
    return price_per_month;
}

void Plan::setPricePerMonth(int pricePerMonth) {
    price_per_month = pricePerMonth;
}

int Plan::getAllowedItemsPerMonth() const {
    return allowed_items_per_month;
}

void Plan::setAllowedItemsPerMonth(int allowedItemsPerMonth) {
    allowed_items_per_month = allowedItemsPerMonth;
}
