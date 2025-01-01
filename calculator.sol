// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract Calculator {
    uint256 result = 0;
    function add (uint256 num) public {
        result += num;
    }
    function substract (uint256 num) public {
        result -= num;
    }
    function multiply (uint256 num) public {
        result *= num;
    }
    function divide (uint256 num) public {
        result /= num;
    }
    function multiply_by_10 () public {
        result *= 10;
    }
    function get () public view returns (uint256) {
        return result;
    }
}