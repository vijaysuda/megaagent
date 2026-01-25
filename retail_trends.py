#!/usr/bin/env python3
"""
Retail Trends Analyzer

A comprehensive tool for analyzing retail sales data and identifying trends.
"""

import json
import csv
from datetime import datetime
from typing import List, Dict, Tuple
from collections import defaultdict
import statistics


class RetailData:
    """Represents a single retail transaction or sales record."""
    
    def __init__(self, date: str, product: str, category: str, quantity: int, revenue: float):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.product = product
        self.category = category
        self.quantity = quantity
        self.revenue = revenue
    
    def __repr__(self):
        return f"RetailData({self.date.strftime('%Y-%m-%d')}, {self.product}, {self.category}, {self.quantity}, ${self.revenue:.2f})"


class RetailTrendsAnalyzer:
    """Analyzes retail data to identify trends and patterns."""
    
    def __init__(self):
        self.data: List[RetailData] = []
    
    def load_from_csv(self, filename: str):
        """Load retail data from a CSV file."""
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = RetailData(
                    date=row['date'],
                    product=row['product'],
                    category=row['category'],
                    quantity=int(row['quantity']),
                    revenue=float(row['revenue'])
                )
                self.data.append(record)
        print(f"Loaded {len(self.data)} records from {filename}")
    
    def load_from_json(self, filename: str):
        """Load retail data from a JSON file."""
        with open(filename, 'r') as f:
            records = json.load(f)
            for record in records:
                self.data.append(RetailData(
                    date=record['date'],
                    product=record['product'],
                    category=record['category'],
                    quantity=record['quantity'],
                    revenue=record['revenue']
                ))
        print(f"Loaded {len(self.data)} records from {filename}")
    
    def analyze_by_category(self) -> Dict[str, Dict[str, float]]:
        """Analyze sales by category."""
        category_stats = defaultdict(lambda: {'total_revenue': 0.0, 'total_quantity': 0, 'count': 0})
        
        for record in self.data:
            stats = category_stats[record.category]
            stats['total_revenue'] += record.revenue
            stats['total_quantity'] += record.quantity
            stats['count'] += 1
        
        # Calculate averages
        for category, stats in category_stats.items():
            stats['avg_revenue'] = stats['total_revenue'] / stats['count']
            stats['avg_quantity'] = stats['total_quantity'] / stats['count']
        
        return dict(category_stats)
    
    def analyze_by_product(self) -> Dict[str, Dict[str, float]]:
        """Analyze sales by product."""
        product_stats = defaultdict(lambda: {'total_revenue': 0.0, 'total_quantity': 0, 'count': 0})
        
        for record in self.data:
            stats = product_stats[record.product]
            stats['total_revenue'] += record.revenue
            stats['total_quantity'] += record.quantity
            stats['count'] += 1
        
        return dict(product_stats)
    
    def identify_top_products(self, n: int = 5) -> List[Tuple[str, float]]:
        """Identify top N products by revenue."""
        product_stats = self.analyze_by_product()
        sorted_products = sorted(
            product_stats.items(),
            key=lambda x: x[1]['total_revenue'],
            reverse=True
        )
        return [(product, stats['total_revenue']) for product, stats in sorted_products[:n]]
    
    def identify_trending_categories(self) -> List[Tuple[str, float]]:
        """Identify trending categories by total revenue."""
        category_stats = self.analyze_by_category()
        sorted_categories = sorted(
            category_stats.items(),
            key=lambda x: x[1]['total_revenue'],
            reverse=True
        )
        return [(category, stats['total_revenue']) for category, stats in sorted_categories]
    
    def calculate_growth_rate(self) -> Dict[str, float]:
        """Calculate growth rate by comparing first and second half of data."""
        if len(self.data) < 2:
            return {}
        
        # Sort data by date
        sorted_data = sorted(self.data, key=lambda x: x.date)
        mid_point = len(sorted_data) // 2
        
        first_half = sorted_data[:mid_point]
        second_half = sorted_data[mid_point:]
        
        first_half_revenue = sum(record.revenue for record in first_half)
        second_half_revenue = sum(record.revenue for record in second_half)
        
        if first_half_revenue > 0:
            growth_rate = ((second_half_revenue - first_half_revenue) / first_half_revenue) * 100
        else:
            growth_rate = 0.0
        
        return {
            'first_half_revenue': first_half_revenue,
            'second_half_revenue': second_half_revenue,
            'growth_rate_percent': growth_rate
        }
    
    def generate_summary_report(self) -> str:
        """Generate a comprehensive summary report."""
        if not self.data:
            return "No data available for analysis."
        
        report = []
        report.append("=" * 60)
        report.append("RETAIL TRENDS ANALYSIS REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Basic statistics
        total_revenue = sum(record.revenue for record in self.data)
        total_quantity = sum(record.quantity for record in self.data)
        report.append(f"Total Records: {len(self.data)}")
        report.append(f"Total Revenue: ${total_revenue:,.2f}")
        report.append(f"Total Quantity Sold: {total_quantity:,}")
        report.append(f"Average Revenue per Transaction: ${total_revenue / len(self.data):,.2f}")
        report.append("")
        
        # Top products
        report.append("-" * 60)
        report.append("TOP 5 PRODUCTS BY REVENUE")
        report.append("-" * 60)
        top_products = self.identify_top_products(5)
        for i, (product, revenue) in enumerate(top_products, 1):
            report.append(f"{i}. {product}: ${revenue:,.2f}")
        report.append("")
        
        # Category analysis
        report.append("-" * 60)
        report.append("CATEGORY PERFORMANCE")
        report.append("-" * 60)
        trending_categories = self.identify_trending_categories()
        for category, revenue in trending_categories:
            report.append(f"{category}: ${revenue:,.2f}")
        report.append("")
        
        # Growth analysis
        report.append("-" * 60)
        report.append("GROWTH ANALYSIS")
        report.append("-" * 60)
        growth_data = self.calculate_growth_rate()
        if growth_data:
            report.append(f"First Half Revenue: ${growth_data['first_half_revenue']:,.2f}")
            report.append(f"Second Half Revenue: ${growth_data['second_half_revenue']:,.2f}")
            report.append(f"Growth Rate: {growth_data['growth_rate_percent']:.2f}%")
        report.append("")
        
        report.append("=" * 60)
        
        return "\n".join(report)


def main():
    """Main function to run the retail trends analyzer."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Retail Trends Analyzer - Analyze retail sales data and identify trends'
    )
    parser.add_argument(
        'input_file',
        help='Input data file (CSV or JSON format)'
    )
    parser.add_argument(
        '--format',
        choices=['csv', 'json'],
        default='csv',
        help='Input file format (default: csv)'
    )
    parser.add_argument(
        '--output',
        help='Output file for the report (optional, prints to console if not specified)'
    )
    
    args = parser.parse_args()
    
    # Create analyzer and load data
    analyzer = RetailTrendsAnalyzer()
    
    try:
        if args.format == 'csv':
            analyzer.load_from_csv(args.input_file)
        else:
            analyzer.load_from_json(args.input_file)
        
        # Generate report
        report = analyzer.generate_summary_report()
        
        # Output report
        if args.output:
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"Report saved to {args.output}")
        else:
            print(report)
    
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
