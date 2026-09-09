def solution(chicken):
    coupon = chicken
    service = 0
    
    while coupon >= 10:
        ch_service = coupon // 10
        service += ch_service
        coupon = (coupon % 10) + ch_service
        
    return service