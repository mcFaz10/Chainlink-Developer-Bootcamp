pragma solidity 0.7.3;
 
contract FirstBrownie {
 
    uint256 number;
 
 
    function setNumber(uint256 _num) public {
        number = _num;
    }
 
    function getNumber() public view returns (uint256){
        return number;
    }

    function addNum(uint256 _num) public view returns (uint256){
        return number+_num;
    }

}
 
