"use client"

import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from "@/components/ui/navigation-menu"
import { Button } from "@/components/ui/button"
import Link from "next/link"
import {Moon, Sun} from "lucide-react"
import { useTheme } from "next-themes"

export default function Navbar() {

  const { theme, setTheme } = useTheme()

  return (
    <nav className="p-8">
      <NavigationMenu>
        <NavigationMenuList>
          <h1 className="font-bold mr-6">APB Trainer v2</h1>
          <NavigationMenuItem>
            <NavigationMenuTrigger>Learn</NavigationMenuTrigger>
            <NavigationMenuContent>
              <NavigationMenuLink
                render={<Link href="/learn/lxs-algorithms" />}
              >
                LXS Algorithms
              </NavigationMenuLink>
              <NavigationMenuLink
                render={<Link href="/learn/eo-pair-algorithms" />}
              >
                EO Pair Algorithms
              </NavigationMenuLink>
              <NavigationMenuLink
                render={<Link href="/learn/resources" />}
              >
                Resources
              </NavigationMenuLink>
            </NavigationMenuContent>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <NavigationMenuTrigger>Practice</NavigationMenuTrigger>
            <NavigationMenuContent>
              <NavigationMenuLink
                render={<Link href="/practice/lxs-trainer" />}
              >
                LXS Trainer
              </NavigationMenuLink>
              <NavigationMenuLink
                render={<Link href="/practice/eo-pair-trainer" />}
              >
                EO Pair Trainer
              </NavigationMenuLink>
            </NavigationMenuContent>
          </NavigationMenuItem>
          <Button variant="outline" className="ml-6" onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>
            <Sun className="h-[1.2rem] w-[1.2rem] scale-100 rotate-0 transition-all dark:scale-0 dark:-rotate-90" />
            <Moon className="absolute h-[1.2rem] w-[1.2rem] scale-0 rotate-90 transition-all dark:scale-100 dark:rotate-0" />
          </Button>
        </NavigationMenuList>
      </NavigationMenu>
    </nav>
  )
}