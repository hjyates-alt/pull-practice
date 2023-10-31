select * from bank.accounts;
use bank;
select 
account_holder_name,
account_holder_surname,
balance,
is_eligible(balance)
from 
bank.accounts;