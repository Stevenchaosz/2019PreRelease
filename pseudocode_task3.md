```pseudocode
DECLARE sold_list: ARRAY[1 : number_of_items] OF STRING

total_fee <- 0

sold <- 0

no_bids <- 0

reserve_not_met <- 0

FOR i <- 1  TO number_of_items

	IF current_highest_bid[i] >= reserve_price_list[i]

		THEN 

			sold_list[i] <- 'sold'

			total_fee <- current_highest_bid[i] * 0.1

			sold <- sold + 1

	ENDIF

NEXT

OUTPUT "Total fee: $", total_fee

FOR i <- 1 TO number_of_items

	IF current_highest_bid[i] < reserve_price_list[i]

		THEN

			IF number_highest_bid[i] > 0

				THEN

					OUTPUT "Item number: ", item_number[i], "- Final bid $", current_highest_bid[i]

					reserve_not_met <- reserve_not_met + 1

				ELSE

					OUTPUT "Item number: ", item_number[i], "no bid"

				no_bids <- no_bids + 1

					reserve_not_met <- reserve_not_met + 1



OUTPUT "Number of items sold: ", sold

OUTPUT "Number of items not meeting reserve: ", reserve_not_met

OUTPUT "Number of items with no bids: ", no_bids

```

