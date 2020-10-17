package com.shoppingList;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.*;

@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
public class ShoppingItem {

    private Long id;
    private String name;
    private Integer amount;
    private Boolean bought;

}
