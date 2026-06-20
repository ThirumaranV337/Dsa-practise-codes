class Solution:
    def medianOf2(self, a, b):
        a.extend(b)
        a.sort()
        length=len(a)-1
        mid=(0+length)//2
        checker=len(a)%2
        if checker==0:
            return (a[mid]+a[mid+1])/2
        else:
            return a[mid]
            
        
